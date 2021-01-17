<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          Reverse Chess Game
        </q-toolbar-title>

        <div v-if="currentUser">
          <q-btn flat label="Sign out" @click="signOut()" />
        </div>
        <div v-else>
          <q-btn flat label="Sign in with Google" @click="signIn()" />
        </div>
      </q-toolbar>
    </q-header>


    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Github',
    caption: 'github.com/alexastrum/firebase-sbhacks-workshop',
    icon: 'code',
    link: 'https://github.com/alexastrum/firebase-vue-sbhacks-workshop'
  },
  {
    title: 'Firebase Docs',
    caption: 'The serverless secret sause',
    icon: 'school',
    link: 'https://firebase.google.com/'
  },
  {
    title: 'Vuejs Docs',
    caption: 'The web app secret sauce',
    icon: 'school',
    link: 'https://v3.vuejs.org/guide'
  },
  {
    title: 'Quasar Docs',
    caption: 'Cross-platform Material Design framework',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'SBHacks VII',
    caption: 'Hackathon official website',
    icon: 'favorite',
    link: 'https://sbhacks.com/'
  }
]

import { defineComponent, ref } from '@vue/composition-api'
import { useFirebase } from '../firebase'

export default defineComponent({
  name: 'MainLayout',
  components: { EssentialLink },
  setup () {
    const leftDrawerOpen = ref(false)
    const essentialLinks = ref(linksData)

    return { leftDrawerOpen, essentialLinks, ...useFirebase() }
  }
})
</script>
