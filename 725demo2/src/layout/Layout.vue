<template>
  <div>
    <div style="display: flex">
      <Aside />
      <router-view style="flex: 1"/>
    </div>
  </div>
</template>

<script>
import Aside from "@/components/Aside";
export default {
  name: "Layout",
  components: {
    Aside
  },
  data() {
    return {
      user: {}
    }
  },
  created() {
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
