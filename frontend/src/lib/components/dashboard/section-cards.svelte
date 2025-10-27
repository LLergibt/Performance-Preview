<script lang="ts">
  import { Badge } from "$lib/components/ui/badge/index.js";
  import * as Table from "$lib/components/ui/table/index.js";
  import ChevronsUpDownIcon from "@lucide/svelte/icons/chevrons-up-down";
</script>
<div class="w-[1150px] flex items-start gap-0">
    <Table.Root>
        <Table.Header>
           <Table.Row>
               <Table.Head class="w-[100px]">Список</Table.Head>
               <Table.Head>Статус</Table.Head>
               <Table.Head class="text-right">Приоритет</Table.Head>
           </Table.Row>
        </Table.Header>
        <Table.Body>
             <Table.Row>
               <Table.Cell class="font-medium"><Badge variant="outline">Название задачи</Badge></Table.Cell>
               <Table.Cell>Задача 1</Table.Cell>
               <Table.Cell>В процессе</Table.Cell>
               <Table.Cell class="text-right">Базовый</Table.Cell>
             </Table.Row>
             <Table.Row>
               <Table.Cell class="font-medium"><Badge variant="outline">Название задачи</Badge></Table.Cell>
               <Table.Cell>Задача 2</Table.Cell>
               <Table.Cell>В процессе</Table.Cell>
               <Table.Cell class="text-right">Базовый</Table.Cell>
             </Table.Row>
             <Table.Row>
               <Table.Cell class="font-medium"><Badge variant="outline">Название задачи</Badge></Table.Cell>
               <Table.Cell>Задача 3</Table.Cell>
               <Table.Cell>В процессе</Table.Cell>
               <Table.Cell class="text-right">Базовый</Table.Cell>
             </Table.Row>
             <Table.Row>
               <Table.Cell class="font-medium"><Badge variant="outline">Название задачи</Badge></Table.Cell>
               <Table.Cell>Задача 4</Table.Cell>
               <Table.Cell>В процессе</Table.Cell>
               <Table.Cell class="text-right">Базовый</Table.Cell>
             </Table.Row>
             <Table.Row>
               <Table.Cell class="font-medium"><Badge variant="outline">Название задачи</Badge></Table.Cell>
               <Table.Cell>Задача 5</Table.Cell>
               <Table.Cell>В процессе</Table.Cell>
               <Table.Cell class="text-right">Базовый</Table.Cell>
             </Table.Row>
         </Table.Body>
     </Table.Root>
</div>