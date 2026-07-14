import { MessageCircle, Send, MessageSquare, Gamepad2 } from 'lucide-react';

export const SERVICES = {
  whatsapp: {
    name: "WhatsApp Business",
    description: "Send and receive messages via WhatsApp Business Cloud API",
    icon: MessageCircle,
    styles: {
      card: "bg-green-50 border-green-200",
      badge: "bg-green-100 text-green-700",
      dot: "bg-green-500",
      button: "bg-green-600 hover:bg-green-700",
      iconWrap: "bg-green-100 text-green-600"
    },
    fields: [
      { key: "primary_credential", label: "Access Token", type: "password", placeholder: "EAAxxxxxxxxxxxxxxxxx..." },
      { key: "secondary_credential", label: "Phone Number ID", type: "text", placeholder: "123456789" },
      { key: "tertiary_credential", label: "Verify Token", type: "text", placeholder: "your_verify_token" }
    ],
    docsUrl: "https://developers.facebook.com/docs/whatsapp/cloud-api"
  },
  telegram: {
    name: "Telegram Bot",
    description: "Send messages and manage bots via Telegram Bot API",
    icon: Send,
    styles: {
      card: "bg-sky-50 border-sky-200",
      badge: "bg-sky-100 text-sky-700",
      dot: "bg-sky-500",
      button: "bg-sky-600 hover:bg-sky-700",
      iconWrap: "bg-sky-100 text-sky-600"
    },
    fields: [
      { key: "primary_credential", label: "Bot Token", type: "password", placeholder: "123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" }
    ],
    docsUrl: "https://core.telegram.org/bots/api"
  },
  discord: {
    name: "Discord Bot",
    description: "Send messages via Discord Webhook and Bot API",
    icon: MessageSquare,
    styles: {
      card: "bg-indigo-50 border-indigo-200",
      badge: "bg-indigo-100 text-indigo-700",
      dot: "bg-indigo-500",
      button: "bg-indigo-600 hover:bg-indigo-700",
      iconWrap: "bg-indigo-100 text-indigo-600"
    },
    fields: [
      { key: "primary_credential", label: "Bot Token", type: "password", placeholder: "MTk8NjI5NDI1MjUyNDQzNjQy.GxqRBN.something" },
      { key: "secondary_credential", label: "Application ID", type: "text", placeholder: "123456789012345678" },
      { key: "webhook_url", label: "Webhook URL", type: "text", placeholder: "https://discord.com/api/webhooks/..." }
    ],
    docsUrl: "https://discord.com/developers/docs/intro"
  },
  steam: {
    name: "Steam Web API",
    description: "Access player data, game info, and Steam inventory",
    icon: Gamepad2,
    styles: {
      card: "bg-slate-50 border-slate-300",
      badge: "bg-slate-200 text-slate-700",
      dot: "bg-slate-600",
      button: "bg-slate-700 hover:bg-slate-800",
      iconWrap: "bg-slate-200 text-slate-600"
    },
    fields: [
      { key: "primary_credential", label: "API Key", type: "password", placeholder: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" },
      { key: "secondary_credential", label: "Steam ID", type: "text", placeholder: "76561197960435530" }
    ],
    docsUrl: "https://steamcommunity.com/dev"
  }
};

export const SERVICE_KEYS = Object.keys(SERVICES);
