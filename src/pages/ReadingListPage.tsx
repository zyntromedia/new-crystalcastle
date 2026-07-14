import { useState } from "react";
import { Link } from "react-router-dom";
import { Bookmark, ArrowRight, BookOpen } from "lucide-react";
import { getReadingList, removeFromReadingList } from "@/hooks/useReadingList";
import { POSTS, CATEGORY_COLORS } from "@/constants/posts";
import PostCard from "@/components/features/PostCard";
import { toast } from "sonner";

export default function ReadingListPage() {
  const [slugs, setSlugs] = useState<string[]>(() => getReadingList());

  const saved = slugs
    .map((slug) => POSTS.find((p) => p.slug === slug))
    .filter(Boolean) as typeof POSTS;

  const handleRemove = (slug: string) => {
    removeFromReadingList(slug);
    setSlugs((prev) => prev.filter((s) => s !== slug));
    toast.success("Removed from reading list.");
  };

  return (
    <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      {/* Header */}
      <div className="flex items-center gap-4 mb-10">
        <div className="w-12 h-12 bg-brand-teal-pale rounded-xl flex items-center justify-center">
          <Bookmark className="w-5 h-5 text-brand-teal" />
        </div>
        <div>
          <h1 className="heading-serif text-3xl sm:text-4xl text-brand-navy dark:text-white">
            Reading List
          </h1>
          <p className="text-brand-muted text-sm mt-0.5">
            {saved.length > 0
              ? `${saved.length} article${saved.length !== 1 ? "s" : ""} saved for later`
              : "Articles you bookmark will appear here"}
          </p>
        </div>
      </div>

      {/* Empty state */}
      {saved.length === 0 && (
        <div className="text-center py-24 border-2 border-dashed border-brand-border rounded-2xl">
          <div className="w-16 h-16 bg-brand-surface rounded-2xl flex items-center justify-center mx-auto mb-5">
            <BookOpen className="w-7 h-7 text-brand-subtle" />
          </div>
          <p className="text-brand-muted text-lg font-medium mb-2">
            Your reading list is empty
          </p>
          <p className="text-brand-subtle text-sm mb-7 max-w-sm mx-auto">
            Click the bookmark icon on any article or card to save it for later.
          </p>
          <Link to="/blog" className="btn-primary">
            Browse Articles <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      )}

      {/* Article grid with remove button overlay */}
      {saved.length > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {saved.map((post) => (
            <div key={post.slug} className="relative group">
              <PostCard post={post} />
              <button
                onClick={() => handleRemove(post.slug)}
                title="Remove from reading list"
                className="absolute top-3 right-3 w-8 h-8 rounded-lg bg-white/90 dark:bg-gray-900/90 border border-brand-border shadow-sm flex items-center justify-center text-brand-teal hover:text-rose-500 hover:border-rose-300 opacity-0 group-hover:opacity-100 transition-all duration-200 z-10"
              >
                <Bookmark className="w-4 h-4 fill-current" />
              </button>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
