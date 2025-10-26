import { superValidate } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import { supervisorSchema } from '$lib/schemas/auth';
import { fail } from '@sveltejs/kit';
import { message } from 'sveltekit-superforms';

export const load = async () => {
	const form = await superValidate(zod4(supervisorSchema));
	return { form };
};

export const actions = {
	default: async ({ request }) => {
		const form = await superValidate(request, zod4(supervisorSchema));
		if (!form.valid) {
			return fail(400, { form });
		}
		return message(form, 'Form submitted successfully!');
	}
};
