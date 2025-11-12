<script lang="ts">
	import { superForm } from 'sveltekit-superforms';
	import SignupForm from '$lib/components/signup-form.svelte';
	import { updateUser } from '$lib/store/auth.js';

	const { data, form: actionData } = $props();

	const { form, errors, enhance } = superForm(data.form);
	$effect(() => {
		if (actionData) {
			console.log(actionData);
			updateUser(actionData?.form.data.access_token);
		}
	});
</script>

<div>
	<div class="flex items-center justify-center min-h-screen bg-[#F7F6F2]">
		<SignupForm {form} {errors} {enhance} />
	</div>
</div>
