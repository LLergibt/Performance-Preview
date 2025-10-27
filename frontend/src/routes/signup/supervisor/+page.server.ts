import { superValidate } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import { supervisorSchema } from '$lib/schemas/auth';
import { fail } from '@sveltejs/kit';
import type { RequestEvent } from '@sveltejs/kit';
import { message } from 'sveltekit-superforms';
import { AuthGateaway } from '$lib/gateways/auth';
const gateway = new AuthGateaway();
export const load = async () => {
	const form = await superValidate(zod4(supervisorSchema));
	return { form };
};

export const actions = {
	default: async (event: RequestEvent) => {
		const { request } = event;
		const form = await superValidate(request, zod4(supervisorSchema));
		if (!form.valid) {
			return fail(400, { form });
		}
		try {
			const data = await gateway.connectToDB();
			console.log(data);
			return message(form, 'Form submitted successfully!');
		} catch (e) {
			const error = e as Error;
			return message(form, `API ERROR: ${error.message}`, { status: 500 });
		}
	}
};
