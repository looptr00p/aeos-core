import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const dashboardRoot = dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  plugins: [react()],
  server: {
    open: true,
    fs: {
      allow: [
        dashboardRoot,
        join(dashboardRoot, "generated"),
      ],
    },
  },
  publicDir: "generated",
});
