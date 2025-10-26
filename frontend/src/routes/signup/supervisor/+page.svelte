<script lang="ts">
	import { superForm } from 'sveltekit-superforms';
	import SignupForm from '$lib/components/signup-Form.svelte';

	const { data } = $props();

	const { form, errors, enhance } = superForm(data.form);
</script>

<div>
	<div class="flex items-center justify-center min-h-screen bg-[#F7F6F2]">
		<SignupForm {form} {errors} {enhance} />
	</div>
</div>
