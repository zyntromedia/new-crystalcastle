import type { LucideIcon } from "lucide-react";

export type AccentKey = "primary" | "accent" | "violet";

export interface TeamMember {
  id: string;
  name: string;
  role: string;
  specialty: string;
  avatar: string;
  accent: AccentKey;
  greeting: string;
}

export interface FeatureModule {
  id: string;
  name: string;
  description: string;
  icon: LucideIcon;
  recommendedBy: string;
}

export interface ProjectData {
  appType: string;
  audience: string;
  goal: string;
}

export interface OnboardingState {
  step: number;
  project: ProjectData;
  features: string[];
}
