import { toast } from "sonner";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { cn } from "@/lib/utils";
import { useOnboarding } from "@/hooks/useOnboarding";
import { StepIndicator } from "@/components/onboarding/StepIndicator";
import { WelcomeStep } from "@/components/onboarding/steps/WelcomeStep";
import { ProjectStep } from "@/components/onboarding/steps/ProjectStep";
import { FeaturesStep } from "@/components/onboarding/steps/FeaturesStep";
import { BuildStep } from "@/components/onboarding/steps/BuildStep";
import { LaunchStep } from "@/components/onboarding/steps/LaunchStep";

export function OnboardingWizard() {
  const { state, goTo, next, back, updateProject, toggleFeature, reset } =
    useOnboarding();
  const { step, project, features } = state;

  const handleProjectNext = () => {
    if (!project.appType.trim()) {
      toast.error("Tell the team what you want to build first.");
      return;
    }
    next();
  };

  const handleFeaturesNext = () => {
    if (features.length === 0) {
      toast.error("Pick at least one feature to include.");
      return;
    }
    next();
  };

  const showDefaultFooter = step === 1 || step === 2;

  return (
    <div className="relative min-h-screen grid-bg">
      <div className="mx-auto flex min-h-screen max-w-5xl flex-col px-4 py-6 sm:px-6 sm:py-10">
        <header className="mb-8 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-primary text-lg font-bold text-primary-foreground">
              F
            </span>
            <span className="font-display text-xl font-bold tracking-tight">
              Forge
            </span>
          </div>
          <span className="text-sm text-muted-foreground">
            Step {step + 1} of 5
          </span>
        </header>

        <div className="mb-10">
          <StepIndicator current={step} onSelect={goTo} />
        </div>

        <main key={step} className="flex-1 animate-fade-up">
          {step === 0 && <WelcomeStep onNext={next} />}
          {step === 1 && (
            <ProjectStep project={project} onChange={updateProject} />
          )}
          {step === 2 && (
            <FeaturesStep selected={features} onToggle={toggleFeature} />
          )}
          {step === 3 && (
            <BuildStep appName={project.appType} onNext={next} onBack={back} />
          )}
          {step === 4 && (
            <LaunchStep project={project} features={features} onReset={reset} />
          )}
        </main>

        {showDefaultFooter && (
          <footer className="mt-10 flex items-center justify-between">
            <button
              type="button"
              onClick={back}
              className="inline-flex items-center gap-2 rounded-xl border border-border px-5 py-3 text-sm font-semibold text-muted-foreground transition-colors hover:text-foreground"
            >
              <ArrowLeft className="h-4 w-4" />
              Back
            </button>
            <button
              type="button"
              onClick={step === 1 ? handleProjectNext : handleFeaturesNext}
              className={cn(
                "group inline-flex items-center gap-2 rounded-xl bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-glow transition-all duration-200 hover:brightness-110 active:scale-[0.98]"
              )}
            >
              Continue
              <ArrowRight className="h-4 w-4 transition-transform duration-200 group-hover:translate-x-1" />
            </button>
          </footer>
        )}
      </div>
    </div>
  );
}
