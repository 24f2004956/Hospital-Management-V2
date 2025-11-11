<template>
    <div v-if="chartData && chartData.length">
        <canvas ref="chartCanvas"></canvas>
    </div>

    <div v-else class="text-center text-muted p-3">
        No appointment data available.
    </div>
</template>

<script>
import { Chart } from "chart.js/auto";

export default {
    name: "AppointmentsChart",
    props: {
        chartData: {
            type: Array,
            default: () => []
        }
    },
    data() {
        return {
            chartInstance: null
        };
    },
    watch: {
        chartData: {
            handler() {
                this.renderChart();
            },
            deep: true,
            immediate: true
        }
    },
    methods: {
        renderChart() {
            // Wait for DOM to render:
            this.$nextTick(() => {
                const canvas = this.$refs.chartCanvas;

                if (!canvas) {
                    console.warn("⚠️ Chart canvas not available yet.");
                    return;
                }

                const ctx = canvas.getContext("2d");

                if (!ctx) {
                    console.error("❌ Failed to get 2D context.");
                    return;
                }

                // Destroy old chart before creating new one:
                if (this.chartInstance) {
                    this.chartInstance.destroy();
                }

                this.chartInstance = new Chart(ctx, {
                    type: "line",
                    data: {
                        labels: this.chartData.map(d => d.date),
                        datasets: [{
                            label: "Appointments Count",
                            data: this.chartData.map(d => d.count),
                            borderWidth: 2
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });

            });
        }
    },
    beforeUnmount() {
        if (this.chartInstance) {
            this.chartInstance.destroy();
        }
    }
};
</script>

<style scoped>
canvas {
    max-width: 100%;
}
</style>
