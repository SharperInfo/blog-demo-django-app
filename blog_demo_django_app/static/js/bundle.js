import * as Sentry from "@sentry/browser";
window.Sentry = Sentry;

import * as htmx from "htmx.org";
htmx.config.includeIndicatorStyles = false;
