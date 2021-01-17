<template>
    <chessBoard v-bind:showBoard="true" />
</template>

<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api'
import { useFirebase } from 'src/firebase'
import chessBoard from 'components/chessBoard.vue'

export default defineComponent({
  name: 'PageIndex',
  components: {
    chessBoard
  },
  setup () {
    const teamName = ref('')
    return {
      teamName,
      ...useFirebase()
    }
  }
})
</script>


