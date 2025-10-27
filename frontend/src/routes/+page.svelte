<script lang="ts">
	import { superForm } from 'sveltekit-superforms';
	import RoleForm from '$lib/components/role-form.svelte';

	const { data } = $props();

	const { form, errors, enhance } = superForm(data.form);
</script>

<div>
	<div class="flex items-center justify-center min-h-screen bg-[#F7F6F2]">
		<RoleForm {form} {errors} {enhance} />
	</div>
</div>
