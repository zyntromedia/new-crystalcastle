import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  Eye,
  Share2,
  Search,
  Tag,
  Trash2,
  Clock,
  ArrowRight,
  History,
} from "lucide-react";
import {
  getAuditTrail,
  clearAuditTrail,
  type AuditEvent,
} from "@/hooks/useAuditTrail";
import { POSTS, CATEGORY_COLORS } from "@/constants/posts";
import { toast } from "sonner";

const EVENT_META: Record<
  AuditEvent["type"],
  { icon: React.ElementType; label: string; color: string }
> = {
  article_viewed: {
    icon: Eye,
    label: "Article Viewed",
    color: "bg-blue-100 text-blue-700",
  },
  article_shared: {
    icon: Share2,
    label: "Article Shared",
    color: "bg-emerald-100 text-emerald-700",
  },
  search_performed: {
    icon: Search,
    label: "Search",
    color: "bg-amber-100 text-amber-700",
  },
  category_visited: {
    icon: Tag,
    label: "Category Visited",
    color: "bg-violet-100 text-violet-700",
  },
};

function timeAgo(ts: number): string {
  const diff = Date.now() - ts;
  const mins = Math.floor(diff / 60_000);
  const hrs = Math.floor(mins / 60);
  const days = Math.floor(hrs / 24);
  if (mins < 1) return "just now";
  if (mins < 60) return `${mins}m ago`;
  if (hrs < 24) return `${hrs}h ago`;
  return `${days}d ago`;
}

function formatDate(ts: number): string {
  return new Date(ts).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  });
}

type FilterType = "all" | AuditEvent["type"];

export default function AuditTrailPage() {
  const [events, setEvents] = useState<AuditEvent[]>([]);
  const [filter, setFilter] = useState<FilterType>("all");

  useEffect(() => {
    setEvents(getAuditTrail());
  }, []);

  const handleClear = () => {
    clearAuditTrail();
    setEvents([]);
    toast.success("Reading history cleared.");
  };

  const filtered =
    filter === "all" ? events : events.filter((e) => e.type === filter);

  const stats = {
    article_viewed: events.filter((e) => e.type === "article_viewed").length,
    article_shared: events.filter((e) => e.type === "article_shared").length,
    search_performed: events.filter((e) => e.type === "search_performed").length,
    category_visited: events.filter((e) => e.type === "category_visited").length,
  };

  return (
    <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      {/* Header */}
      <div className="flex items-start justify-between mb-8">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-brand-teal-pale rounded-xl flex items-center justify-center">
              <History className="w-5 h-5 text-brand-teal" />
            </div>
            <h1 className="heading-serif text-3xl text-brand-navy dark:text-white">
              Activity Log
            </h1>
          </div>
          <p className="text-brand-muted text-sm ml-13">
            Your reading history, searches, and interactions — stored locally in your browser.
          </p>
        </div>
        {events.length > 0 && (
          <button
            onClick={handleClear}
            className="flex items-center gap-2 text-sm text-rose-500 hover:text-rose-600 hover:bg-rose-50 px-3 py-2 rounded-lg transition-colors"
          >
            <Trash2 className="w-4 h-4" /> Clear all
          </button>
        )}
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8">
        {(Object.entries(stats) as [AuditEvent["type"], number][]).map(([type, count]) => {
          const meta = EVENT_META[type];
          const Icon = meta.icon;
          return (
            <button
              key={type}
              onClick={() => setFilter(filter === type ? "all" : type)}
              className={`p-4 rounded-xl border text-left transition-all ${
                filter === type
                  ? "border-brand-teal bg-brand-teal-pale shadow-sm"
                  : "border-brand-border bg-white dark:bg-gray-900 hover:border-brand-teal/50"
              }`}
            >
              <div className={`w-7 h-7 rounded-lg flex items-center justify-center mb-2 ${meta.color}`}>
                <Icon className="w-3.5 h-3.5" />
              </div>
              <p className="text-2xl font-bold text-brand-navy dark:text-white leading-none">
                {count}
              </p>
              <p className="text-brand-subtle text-xs mt-0.5">{meta.label}</p>
            </button>
          );
        })}
      </div>

      {/* Filter tabs */}
      <div className="flex gap-2 mb-6 flex-wrap">
        {(["all", "article_viewed", "article_shared", "search_performed", "category_visited"] as const).map((f) => (
          <button
            key={f}
            onClick={() => setFilter(f)}
            className={`text-xs px-3 py-1.5 rounded-full border transition-colors ${
              filter === f
                ? "bg-brand-teal text-white border-brand-teal"
                : "border-brand-border text-brand-muted hover:border-brand-teal hover:text-brand-teal"
            }`}
          >
            {f === "all" ? "All activity" : EVENT_META[f].label}
          </button>
        ))}
      </div>

      {/* Empty state */}
      {events.length === 0 && (
        <div className="text-center py-20">
          <div className="w-16 h-16 bg-brand-surface rounded-2xl flex items-center justify-center mx-auto mb-5">
            <Clock className="w-7 h-7 text-brand-subtle" />
          </div>
          <p className="text-brand-muted text-lg font-medium mb-2">
            No activity yet
          </p>
          <p className="text-brand-subtle text-sm mb-6 max-w-sm mx-auto">
            As you read articles, search, and explore categories, your activity will appear here.
          </p>
          <Link to="/blog" className="btn-primary">
            Start Reading <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      )}

      {/* Events list */}
      {filtered.length > 0 && (
        <div className="space-y-2">
          {filtered.map((event) => {
            const meta = EVENT_META[event.type];
            const Icon = meta.icon;
            const post = event.slug ? POSTS.find((p) => p.slug === event.slug) : undefined;
            const catColor = post ? CATEGORY_COLORS[post.category] || "" : "";

            return (
              <div
                key={event.id}
                className="flex items-center gap-4 bg-white dark:bg-gray-900 border border-brand-border dark:border-gray-700 rounded-xl px-4 py-3 hover:border-brand-teal/40 transition-colors group"
              >
                <div className={`w-8 h-8 rounded-lg flex items-center justify-center shrink-0 ${meta.color}`}>
                  <Icon className="w-3.5 h-3.5" />
                </div>

                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-0.5">
                    <span className="text-xs text-brand-subtle font-medium">
                      {meta.label}
                    </span>
                    {post && (
                      <span className={`tag-pill text-[10px] py-0 px-2 ${catColor}`}>
                        {post.category}
                      </span>
                    )}
                  </div>
                  {event.slug && post ? (
                    <Link
                      to={`/blog/${event.slug}`}
                      className="text-sm font-medium text-brand-charcoal dark:text-white hover:text-brand-teal transition-colors truncate block"
                    >
                      {event.label}
                    </Link>
                  ) : (
                    <p className="text-sm font-medium text-brand-charcoal dark:text-white truncate">
                      {event.type === "search_performed"
                        ? `"${event.label}"`
                        : event.label}
                    </p>
                  )}
                </div>

                <div className="text-right shrink-0">
                  <p className="text-xs text-brand-subtle">{timeAgo(event.timestamp)}</p>
                  <p className="text-[10px] text-brand-subtle/60 hidden group-hover:block">
                    {formatDate(event.timestamp)}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {filtered.length === 0 && events.length > 0 && (
        <div className="text-center py-12 text-brand-subtle">
          No events of this type yet.
        </div>
      )}
    </main>
  );
}
