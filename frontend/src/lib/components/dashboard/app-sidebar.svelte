<script lang="ts">
  import StarIcon from "@lucide/svelte/icons/star";
  import CrownIcon from "@lucide/svelte/icons/crown";
  import UserIcon from "@lucide/svelte/icons/user";
  import MessageCircleIcon from "@lucide/svelte/icons/message-circle";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import NavMain from "./nav-main.svelte";
  import NavUser from "./nav-user.svelte";
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
  import type { ComponentProps } from "svelte";
  const data = {
    user: {
      name: "Шрек Оргович",
      email: "goshaPDF@turma.com",
      avatar: "http://images-s.kinorium.com/movie/promo/237554/w1500_50027112.jpg",
    },
    navMain: [
      {
        title: "Рейтинг",
        url: "#",
        icon: CrownIcon,
      },
      {
        title: "Отзывы",
        url: "#",
        icon: MessageCircleIcon,
      },
      {
        title: "Оценки",
        url: "#",
        icon: StarIcon,
      },
      {
        title: "Личный кабинет",
        url: "#",
        icon: UserIcon,
      },
      {
        title: "Настройки",
        url: "#",
        icon: SettingsIcon,
      },
    ],
  };
  let { ...restProps }: ComponentProps<typeof Sidebar.Root> = $props();
</script>
<Sidebar.Root collapsible="offcanvas" {...restProps}>
  <Sidebar.Header>
    <NavUser user={data.user} />
  </Sidebar.Header>
  <Sidebar.Content>
    <NavMain items={data.navMain} />
  </Sidebar.Content>
</Sidebar.Root>