import { superValidate } from 'sveltekit-superforms';
import type { Infer, SuperValidated } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';

import { loginSchema, tokenSchema, type loginData } from '$lib/schemas/auth';
import { fail, redirect } from '@sveltejs/kit';
import type { RequestEvent } from '@sveltejs/kit';
import { message } from 'sveltekit-superforms';
import { AuthGateaway } from '$lib/gateways/auth';
const gateway = new AuthGateaway();
export const load = async () => {
	const form = await superValidate(zod4(loginSchema));
	return { form };
};

export const actions = {
	default: async (event: RequestEvent) => {
		const { request } = event;
		const form = await superValidate(request, zod4(loginSchema));
		if (!form.valid) {
			return fail(400, { form });
		}
		try {
			const result: loginData = {
				email: form.data.email,
				password: form.data.password
			};
			const tokenRaw = await gateway.signUserIn(result);
			const token = await superValidate(tokenRaw, zod4(tokenSchema));
			

			event.cookies.set('AuthorizationToken', `Bearer ${token.data.refresh_token}`, {
				httpOnly: true,
				path: '/',
				secure: import.meta.env.VITE_BEHAVIOR === 'production',
				sameSite: 'strict',
				maxAge: 60 * 43800
			});
			return message(token, 'Form submitted successfully!');
		} catch (e) {
			const error = e as Error;
			return message(form, `API ERROR: ${error.message}`, { status: 500 });
			// return fail(400, { form });
		}
		// redirect(302, '/');
	}
};
