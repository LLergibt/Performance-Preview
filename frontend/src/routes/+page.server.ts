import { superValidate } from 'sveltekit-superforms';
import { zod4 } from 'sveltekit-superforms/adapters';
import { signupSchema } from '$lib/schema';
import { fail } from '@sveltejs/kit';
import { message } from 'sveltekit-superforms';

export const load = async () => {
	const form = await superValidate(zod4(signupSchema));
	return { form };
};

export const actions = {
	default: async ({ request }) => {
		const form = await superValidate(request, zod4(signupSchema));
		if (!form.valid) {
			console.log(form);
			return fail(400, { form });
		}
		// TODO: Handle successful submission (e.g., save to DB)
		return message(form, 'Form submitted successfully!');
	}
};
