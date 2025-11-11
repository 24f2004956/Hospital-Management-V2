<template>
  <div v-if="chartData && chartData.length">
    <canvas ref="chartCanvas"></canvas>
  </div>
  <div v-else class="text-center text-muted p-3">
    No department data found.
  </div>
</template>

<script>
import { Chart } from "chart.js/auto";

export default {
  name: "DepartmentDemandChart",
  props: {
    chartData: { type: Array, default: () => [] }
  },
  data() {
    return { chartInstance: null };
  },
  watch: {
    chartData: {
      handler() { this.renderChart(); },
      deep: true,
      immediate: true
    }
  },
  methods: {
    renderChart() {
      this.$nextTick(() => {
        const canvas = this.$refs.chartCanvas;
        if (!canvas) return;

        const ctx = canvas.getContext("2d");
        if (!ctx) return;

        if (this.chartInstance) this.chartInstance.destroy();

        this.chartInstance = new Chart(ctx, {
          type: "bar",
          data: {
            labels: this.chartData.map(d => d.department),
            datasets: [
              {
                label: "Appointments per Department",
                data: this.chartData.map(d => d.count),
                borderWidth: 2,
                backgroundColor: "rgba(54, 162, 235, 0.5)",
                borderColor: "rgba(54, 162, 235, 1)"
              }
            ]
          },
          options: {
            scales: {
              y: { beginAtZero: true }
            }
          }
        });
      });
    }
  },
  beforeUnmount() {
    if (this.chartInstance) this.chartInstance.destroy();
  }
};
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style>
