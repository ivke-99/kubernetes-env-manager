<script>
import ConfigCard from '../components/ConfigCard.vue';

export default {
  components: {
    ConfigCard
  }
}
</script>

<template>
  <div class="configmaps">
    <ConfigCard id="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"/>
    <ConfigCard id="test2"/>
    <ConfigCard id="test3"/>
    <ConfigCard id="test4"/>
  </div>
</template>

<style>
.configmaps {
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	align-content: space-evenly;
}
</style>
