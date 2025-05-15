import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "rice-plant-disease-classification.k-clowd.top",
        pathname: "/api/image/**",
      },
    ],
  },
};

export default nextConfig;
