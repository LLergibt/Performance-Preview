import { superValidate } from 'sveltekit-superforms';
import type { Infer, SuperValidated } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import {
	employeeSchema,
	signupSchema,
	supervisorSchema,
	tokenSchema,
	type signupData
} from '$lib/schemas/auth';
import { fail } from '@sveltejs/kit';
import type { RequestEvent } from '@sveltejs/kit';
import { message } from 'sveltekit-superforms';
import { AuthGateaway } from '$lib/gateways/auth';
const gateway = new AuthGateaway();
export const load = async () => {
	const form = await superValidate(zod4(employeeSchema));
	return { form };
};

export const actions = {
	default: async (event: RequestEvent) => {
		const { request } = event;
		const form = await superValidate(request, zod4(employeeSchema));
		if (!form.valid) {
			return fail(400, { form });
		}
		try {
			const fullname = form.data.fullname.split(' ');
			const result: signupData = {
				lastname: fullname[0],
				firstname: fullname[1],
				surname: fullname[2],
				email: form.data.email,
				password: form.data.password,
				role: form.data.role,
				supervisor_email: form.data.supervisor_email
			};
			const tokenRaw = await gateway.signUserUp(result);
			const token = await superValidate(tokenRaw, zod4(tokenSchema));
			return message(token, 'Form submitted successfully!');
		} catch (e) {
			const error = e as Error;
			return message(form, `API ERROR: ${error.message}`, { status: 500 });
		}
	}
};
