<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';

	const { form, errors, enhance } = $props();
</script>

<Card.Root class="py-30 px-0 w-full max-w-lg">
	<Card.Header class="text-center">
		<div>
			<Card.Title class="text-center text-2xl">Авторизация</Card.Title>
			<Card.Description class="text-sm text-[#71717a]"
				>Введите свои данные для входа в аккаунт</Card.Description
			>
		</div>
	</Card.Header>

	<form class="flex flex-col" method="POST" use:enhance novalidate>
		<Card.Content class="w-full">
			<div class="flex flex-col gap-2 w-full">
				<div class="grid gap-2">
					<Input
						name="email"
						type="email"
						placeholder="Name@gmail.com"
						class="w-full"
						bind:value={$form.email}
						aria-invalid={$errors.email ? 'true' : undefined}
						required
					/>
					{#if $errors.email}<span>{$errors.email}</span>{/if}
				</div>
				<div class="grid gap-2 flex items-center">
					<Input
						name="password"
						type="password"
						placeholder="Пароль"
						class="w-full"
						aria-invalid={$errors.password ? 'true' : undefined}
						bind:value={$form.password}
						required
					/>
					{#if $errors.password}<span>{$errors.password}</span>{/if}
				</div>
			</div>
		</Card.Content>

		<Card.Footer class="flex-col gap-2 w-full pt-6 ">
			<Button type="submit" class="w-full">Войти в аккаунт</Button>
			<Button variant="link"><a href="#" class="text-[#8c8c8c] underline">Забыли пароль?</a></Button
			>
		</Card.Footer>
	</form>

	<div class="flex items-center justify-center -mt-6 pb-15">
		<Card.Action>
			<Label for="account" class="text-[#8c8c8c]"
				>Ещё нет аккаунта?<Button variant="link" class="p-0 m-0"
					><a href="/signup" class="text-[#8c8c8c] underline">Создать</a></Button
				></Label
			>
		</Card.Action>
	</div>
</Card.Root>
