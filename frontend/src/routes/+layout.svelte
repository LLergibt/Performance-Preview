<script lang="ts">
	import { user } from '$lib/store/auth';
	import '../app.css';

	let { children } = $props();
	console.log($user.user);
</script>

<div class="flex flex-col">
	{#if $user.isAuthenticated}
		<div>{$user.user?.email}</div>
	{/if}
	{@render children?.()}
</div>
