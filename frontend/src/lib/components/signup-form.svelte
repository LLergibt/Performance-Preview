<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';

	const { form, errors, enhance, children } = $props();
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
				<div class="grid gap-2">
					<Input
						type="text"
						placeholder="Иванов Иван Иванович"
						name="fullname"
						class="w-full"
						aria-invalid={$errors.fullname ? 'true' : undefined}
						required
						bind:value={$form.fullname}
					/>
					{#if $errors.fullname}<span class="invalid">{$errors.fullname}</span>{/if}
				</div>

				<div class="grid gap-2">
					<Input
						type="email"
						placeholder="name@gmail.com"
						name="email"
						class="w-full"
						aria-invalid={$errors.email ? 'true' : undefined}
						required
						bind:value={$form.email}
					/>
					{#if $errors.email}<span class="invalid">{$errors.email}</span>{/if}
				</div>
				<div class="grid gap-2">
					<Input
						id="password"
						placeholder="Пароль"
						type="password"
						name="password"
						class="w-full"
						aria-invalid={$errors.password ? 'true' : undefined}
						required
						bind:value={$form.password}
					/>
					{#if $errors.password}<span class="invalid">{$errors.password}</span>{/if}
				</div>
				<div class="grid gap-2">
					<Input
						placeholder="Подтвердите пароль"
						type="password"
						name="confirm"
						class="w-full"
						aria-invalid={$errors.confirm ? 'true' : undefined}
						required
						bind:value={$form.confirm}
					/>
					{#if $errors.confirm}<span class="invalid">{$errors.confirm}</span>{/if}
				</div>
				{#if children}
					{@render children()}
				{/if}
			</div>
		</Card.Content>
		<Card.Footer class="flex-col gap-2 w-full pt-6">
			<Button type="submit" class="w-full">Создать аккаунт</Button>
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
