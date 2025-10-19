<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<div class="flex flex-col">
	<h1 class="text-2xl">Performance Review</h1>
	{@render children?.()}
</div>
