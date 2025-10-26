import { fail } from '@sveltejs/kit';
import { message, superValidate } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import { loginSchema } from '$lib/schemas/auth';

export const load = async () => {
	const form = await superValidate(zod4(loginSchema));
	return { form };
};

export const actions = {
	default: async ({ request }) => {
		const form = await superValidate(request, zod4(loginSchema));
		if (!form.valid) {
			return fail(400, { form });
		}
		return message(form, 'Form submitted successfully!');
	}
};
