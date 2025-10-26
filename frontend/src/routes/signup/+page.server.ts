import { fail } from '@sveltejs/kit';
import { message, superValidate } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import { roleSchema } from '$lib/schemas/auth';
import { redirect } from '@sveltejs/kit';

export const load = async () => {
	const form = await superValidate(zod4(roleSchema));
	return { form };
};

export const actions = {
	default: async ({ request }) => {
		const form = await superValidate(request, zod4(roleSchema));
		if (!form.valid) {
			return fail(400, { form });
		}
		redirect(302, `/signup/${form.data.role}`);
		return message(form, 'Form submitted successfully!');
	}
};
