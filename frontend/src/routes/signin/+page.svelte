<script lang="ts">
	import LoginForm from '$lib/components/login-form.svelte';
	import { updateUser, user } from '$lib/store/auth.js';
	import { superForm } from 'sveltekit-superforms';
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
		<LoginForm {form} {errors} {enhance} />
	</div>
</div>
