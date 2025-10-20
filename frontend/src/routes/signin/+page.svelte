<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import * as Card from "$lib/components/ui/card/index.js";
 import './signup.css'
</script>
 
<Card.Root class="w-full max-w-sm">
 <Card.Header>
  <Card.Title>Регистрация</Card.Title>
  <Card.Description
   >Введите свою почту, чтоб зарегистрировать аккаунт</Card.Description
  >
  <Card.Action>
   <Button variant="link">Sign In</Button>
  </Card.Action>
 </Card.Header>
 <Card.Content>
  <form>
   <div class="flex flex-col gap-6">
    <div class="grid gap-2">
     <Label for="firstname">Имя</Label>
     <Input id="firstname" type="firstname" placeholder="Имя" required />
    </div>
    <div class="grid gap-2">
     <Label for="lastname">Фамилия</Label>
     <Input id="lastname" type="lastname" placeholder="Фамилия" required />
    </div>
    <div class="grid gap-2">
     <Label for="surname">Отчество</Label>
     <Input id="surname" type="surname" placeholder="Отчество" required />
    </div>
    <div class="grid gap-2">
     <Label for="email">Email</Label>
     <Input id="email" type="email" placeholder="m@example.com" required />
    </div>
    <div class="grid gap-2">
     <div class="flex items-center">
      <Label for="password">Password</Label>
     </div>
     <Input id="password" type="password" required />
    </div>
    <div class="grid gap-2">
     <div class="flex items-center">
      <Label for="password">Confirm Password</Label>
     </div>
     <Input id="password" type="password" required />
    </div>
   </div>
  </form>
 </Card.Content>
 <Card.Footer class="flex-col gap-2">
  <Button type="submit" class="w-full">Зарегистрироваться</Button>
 </Card.Footer>
</Card.Root>