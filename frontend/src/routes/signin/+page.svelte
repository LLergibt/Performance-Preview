<script lang="ts">
	import LoginForm from '$lib/components/login-form.svelte';
	import { superForm } from 'sveltekit-superforms';

	const { data } = $props();
	const { form, errors, enhance } = superForm(data.form);
</script>

<div>
	<div class="flex items-center justify-center min-h-screen bg-[#F7F6F2]">
		<LoginForm {form} {errors} {enhance} />
	</div>
</div>
