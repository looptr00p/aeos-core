import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { join } from "path";

export default defineConfig({
  plugins: [react()],
  server: {
    open: true,
    fs: {
      allow: [join(__dirname, "generated")],
    },
  },
  publicDir: "generated",
});
