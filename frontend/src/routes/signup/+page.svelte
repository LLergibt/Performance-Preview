<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import * as Card from "$lib/components/ui/card/index.js";
 import '../../app.css';
</script>

<div>
    <div class="flex items-center justify-center min-h-screen bg-[#F7F6F2]">
        <Card.Root class="py-30 px-0 w-full max-w-lg">
            <Card.Header class="text-center">
                <Card.Title class="text-center text-2xl">Регистрация</Card.Title>
                <Card.Description class="text-sm text-[#71717a]">Добавьте свои данные для создания аккаунта</Card.Description>
            </Card.Header>

            <Card.Content class="w-full">
                <form>
                <div class="flex flex-col gap-2 w-full">
                    <!--<div class="grid gap-2">
                        <Input id="lastname" type="text" placeholder="Фамилия" class="w-full" required />
                    </div>---->
                    <div class="grid gap-2">
                        <Input id="name" type="text" placeholder="Иванов Иван Иванович" class="w-full" required />
                    </div>
                    <div class="grid gap-2">
                        <Input id="role" type="text" placeholder="Роль" class="w-full" required />
                    </div>
                    <div class="grid gap-2">
                        <Input id="email" type="email" placeholder="Name@gmail.com" class="w-full" required />
                    </div>
                    <div class="grid gap-2 flex items-center">
                        <Input id="password" type="password" placeholder="Пароль" class="w-full" required />
                    </div>
                    <div class="grid gap-2 flex items-center">
                        <Input id="confirm-password" type="password" placeholder="Подтвердите пароль" class="w-full" required />
                    </div>
                </div>
                </form>
            </Card.Content>

            <Card.Footer class="flex-col gap-2 w-full">
                <Button type="submit" class="w-full">Создать аккаунт</Button>
            </Card.Footer>

            <div class="flex items-center justify-center">
                <Card.Action>
                <Label for="account" class="text-[#8c8c8c]">Уже есть аккаунт?<Button variant="link" class="p-0 m-0"><a href="/signin" class="text-[#8c8c8c] underline">Войти</a></Button></Label>
                </Card.Action>
            </div>
        </Card.Root>
    </div>
</div>