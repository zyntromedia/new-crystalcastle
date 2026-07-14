import { Link } from "react-router-dom";
import { ArrowRight, TrendingUp, Users, Globe } from "lucide-react";
import heroWorkspace from "@/assets/hero-workspace.jpg";
import { POSTS } from "@/constants/posts";
import PostCard from "@/components/features/PostCard";
import Newsletter from "@/components/features/Newsletter";

const stats = [
  { icon: TrendingUp, value: "67%", label: "of companies now offer hybrid or remote options" },
  { icon: Users, value: "92%", label: "of 4-day week trial companies continued permanently" },
  { icon: Globe, value: "65+", label: "countries represented in async-first companies" },
];

export default function HomePage() {
  const featuredPosts = POSTS.filter((p) => p.featured).slice(0, 2);
  const recentPosts = POSTS.filter((p) => !p.featured).slice(0, 3);

  return (
    <main>
      {/* Hero */}
      <section className="relative overflow-hidden min-h-[580px] flex items-center">
        <div className="absolute inset-0">
          <img
            src={heroWorkspace}
            alt="Modern workspace"
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-brand-navy/90 via-brand-navy/60 to-brand-navy/20" />
        </div>

        <div className="relative max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-28">
          <div className="max-w-xl">
            <span className="tag-pill bg-brand-teal/20 text-brand-teal-light mb-5 inline-flex">
              The Future of Work
            </span>
            <h1 className="heading-serif text-4xl sm:text-5xl lg:text-6xl text-white leading-tight mb-5">
              New systems for how we work, live, and lead
            </h1>
            <p className="text-white/70 text-base sm:text-lg leading-relaxed mb-8">
              WorkShift covers the ideas, experiments, and evidence reshaping
              the modern workplace — from 4-day weeks to async culture, from
              remote wellbeing to outcome-based leadership.
            </p>
            <div className="flex flex-wrap gap-3">
              <Link to="/blog" className="btn-primary">
                Explore Articles <ArrowRight className="w-4 h-4" />
              </Link>
              <Link to="/about" className="btn-outline border-white text-white hover:bg-white hover:text-brand-navy">
                About WorkShift
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Bar */}
      <section className="bg-white border-b border-brand-border">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 divide-y sm:divide-y-0 sm:divide-x divide-brand-border">
            {stats.map(({ icon: Icon, value, label }) => (
              <div key={value} className="flex items-center gap-4 sm:px-6 py-2 sm:py-0 first:pl-0">
                <div className="w-10 h-10 bg-brand-teal-pale rounded-lg flex items-center justify-center shrink-0">
                  <Icon className="w-5 h-5 text-brand-teal" />
                </div>
                <div>
                  <p className="font-serif font-bold text-2xl text-brand-navy leading-tight">{value}</p>
                  <p className="text-brand-muted text-xs leading-snug">{label}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Posts */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="heading-serif text-2xl sm:text-3xl text-brand-navy">Featured Stories</h2>
            <p className="text-brand-muted text-sm mt-1">Essential reads on the new world of work</p>
          </div>
          <Link to="/blog" className="hidden sm:flex items-center gap-1 text-brand-teal text-sm font-semibold hover:underline">
            View all <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {featuredPosts.map((post) => (
            <PostCard key={post.id} post={post} featured />
          ))}
        </div>
      </section>

      {/* Recent Posts */}
      <section className="bg-brand-surface border-t border-brand-border py-14">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between mb-8">
            <h2 className="heading-serif text-2xl sm:text-3xl text-brand-navy">Recent Articles</h2>
            <Link to="/blog" className="hidden sm:flex items-center gap-1 text-brand-teal text-sm font-semibold hover:underline">
              All articles <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {recentPosts.map((post) => (
              <PostCard key={post.id} post={post} />
            ))}
          </div>
          <div className="mt-8 text-center sm:hidden">
            <Link to="/blog" className="btn-outline">
              All Articles <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* Newsletter */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        <Newsletter />
      </section>
    </main>
  );
}
