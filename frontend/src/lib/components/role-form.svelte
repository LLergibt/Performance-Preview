<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import { derived } from 'svelte/store';
	import * as Select from '$lib/components/ui/select/index.js';

	const { form, errors, enhance } = $props();
	const roles = [
		{ value: 'supervisor', label: 'Руководитель' },
		{ value: 'employee', label: 'Сотрудник' }
	];

	const roleStore = derived(form, ($f) => $f.role);
	const triggerContent = $derived(
		roles.find((f) => f.value === $roleStore)?.label ?? 'Выберите роль'
	);
</script>

<Card.Root class="py-30 px-0 w-full max-w-lg">
	<Card.Header class="text-center">
		<Card.Title class="text-center text-2xl">Регистрация</Card.Title>
		<Card.Description class="text-sm text-[#71717a]"
			>Добавьте свои данные для создания аккаунта</Card.Description
		>
	</Card.Header>

	<form class="flex flex-col" method="POST" use:enhance novalidate>
		<Card.Content class="w-full">
			<div class="flex flex-col gap-2 w-full">
				<Select.Root type="single" name="role" bind:value={$form.role}>
					<Select.Trigger aria-invalid={$errors.role ? 'true' : undefined} class="w-full">
						{triggerContent}
					</Select.Trigger>
					<Select.Content>
						<Select.Group>
							<Select.Label>Роли</Select.Label>
							{#each roles as role (role.value)}
								<Select.Item value={role.value} label={role.label}>{role.label}</Select.Item>
							{/each}
						</Select.Group>
					</Select.Content>
				</Select.Root>
				{#if $errors.role}<span class="invalid">{$errors.role}</span>{/if}
			</div>
		</Card.Content>
		<Card.Footer class="flex-col gap-2 w-full pt-6">
			<Button type="submit" class="w-full">Продолжить</Button>
		</Card.Footer>
	</form>

	<div class="flex items-center justify-center">
		<Card.Action>
			<Label for="account" class="text-[#8c8c8c]"
				>Уже есть аккаунт?<Button type="submit" variant="link" class="p-0 m-0"
					><a href="/signin" class="text-[#8c8c8c] underline">Войти</a></Button
				></Label
			>
		</Card.Action>
	</div>
</Card.Root>
