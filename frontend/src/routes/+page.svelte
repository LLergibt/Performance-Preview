<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { superForm } from 'sveltekit-superforms';
	import SuperDebug from 'sveltekit-superforms';

	let { data } = $props();

	// Client API:
	const { form, errors, constraints, message, enhance } = superForm(data.form);
</script>

<SuperDebug data={$form} />

<div>
	<form method="POST" use:enhance novalidate>
		<label for="name">Name</label>
		<input
			type="text"
			name="name"
			aria-invalid={$errors.name ? 'true' : undefined}
			bind:value={$form.name}
		/>
		<label for="email">E-mail</label>
		<Input
			type="email"
			name="email"
			aria-invalid={$errors.email ? 'true' : undefined}
			required
			bind:value={$form.email}
		/>
		{#if $errors.email}<span class="invalid">{$errors.email}</span>{/if}
		<label for="password">Password</label>
		<Input
			type="password"
			name="password"
			aria-invalid={$errors.password ? 'true' : undefined}
			bind:value={$form.password}
			required
		/>
		{#if $errors.password}<span class="invalid">{$errors.password}</span>{/if}

		<div><button>Submit</button></div>
	</form>
	<h1>Welcome to Performance Review</h1>
	<p>
		Visit
		<Button class="text-sm m-0 p-0" variant="link"
			><a href="https://github.com/LLergibt/Performance-Preview">Our Github</a></Button
		>

		to learn Performance Review project
	</p>
</div>
