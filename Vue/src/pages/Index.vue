<template>
  <div class="board">
    <div v-for="row in 8" :key="row">
      <div v-for="col in 8" :key="col">
        <chessSquare v-bind:row="row" v-bind:col="col" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import TeamComponent from 'components/TeamComponent.vue'
import { defineComponent, ref } from '@vue/composition-api'
  import { useFirebase } from 'src/firebase'
  import chessSquare from 'components/chessSquare.vue'

export default defineComponent({
  name: 'PageIndex',
  components: {
    TeamComponent,
    chessSquare
  },
  setup () {
    const teamName = ref('')
    return {
      teamName,
      ...useFirebase()
    }
  },
})
</script>

<style>
  {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    min-height: 100vh;
  }

  .upperdiv {
    position: absolute;
    top: 47%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 670px;
    height: 670px;
    font-size: 1.5rem;
  }
  .chessSquare img{
    width: 4vw;
    height: 4vw;
    object-fit: cover;
    grid-row-gap: 0;
  }

  .board {
    position: absolute;
    display: grid;
    grid-template-columns: repeat(8,1fr);
    top: 47%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 5px solid beige;
    height: 650px;
    width: 650px;
  }

  .square {
    height: 75px;
    width: 75px;
  }

  .beige {
    background: beige;
  }

  .sandybrown {
    background: rgb(202, 124, 68);
  }

  .numbers {
    height: 100%;
    width: 5%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    left: 0;
    top: 0;
    text-align: center;
    font-family: 'Times New Roman', Times, serif;
  }

  .letters {
    position: absolute;
    width: 100%;
    bottom: 0;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    font-family: 'Times New Roman', Times, serif;
  }

  li {
    list-style: none;
  }

  h1, h3 {
    text-align: center;
    font-family: 'Times New Roman', Times, serif;
  }
</style>
