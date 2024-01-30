<template>
  <div>
    <Navbar />

    <section class="section">
      <router-view />
    </section>
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue';

export default {
  name: 'App',
  components: {
      Navbar,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    if (this.$store.state.token){
      axios.default.header.common['Authorization'] = "Token " + this.$store.state.token
    } else {
      axios.default.header.common['Authorization'] = ""
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma/'
</style>
