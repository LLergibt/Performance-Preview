<script lang="ts">
	import { superForm } from 'sveltekit-superforms';
	import RoleForm from '$lib/components/role-form.svelte';

	const { data } = $props();

	const { form, errors, enhance } = superForm(data.form);
</script>

<div>
	<h1>Покажи письку</h1>
</div>
