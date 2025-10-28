<script lang="ts">
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';

	import { superForm } from 'sveltekit-superforms';
	import SignupForm from '$lib/components/signup-form.svelte';

	const { data } = $props();

	const { form, errors, enhance } = superForm(data.form);
</script>

<div>
	<div class="flex items-center justify-center min-h-screen bg-[#F7F6F2]">
		<SignupForm {form} {errors} {enhance}>
			<div class="grid gap-2">
				<Label>Почта руководителя</Label>
				<Input
					placeholder="name@gmail.com"
					type="email"
					name="supervisor_email"
					class="w-full"
					aria-invalid={$errors.supervisor_email ? 'true' : undefined}
					required
					bind:value={$form.supervisor_email}
				/>
				{#if $errors.supervisor_email}<span class="invalid">{$errors.supervisor_email}</span>{/if}
			</div>
		</SignupForm>
	</div>
</div>
