# 308 Digital Brand Guidelines

## Overview
308 Digital is an AI consulting firm helping organizations in finance, insurance, healthcare, and retail unlock the potential of Artificial Intelligence. Our brand reflects sophistication, innovation, and expertise.

## Color Palette

### Primary Colors
- **Ink (Dark Navy)**: `#20242b` — Primary text, headings, UI elements
- **Charcoal**: `#2c313a` — Secondary text, navigation
- **Navy Deep**: `#181b21` — Hero background, high-contrast sections

### Accent Colors
- **Orange**: `#ef611c` — Primary call-to-action, highlights, accents
- **Amber**: `#ff9a4d` — Secondary accent, hover states, decorative elements

### Background Colors
- **Paper**: `#f7f4ee` — Primary background
- **Paper 2**: `#efeae0` — Secondary background
- **Cream**: `#f4f1ea` — Light text backgrounds

### Neutral Colors
- **Slate**: `#565c6b` — Supporting text, metadata
- **Line**: `rgba(32,36,43,0.12)` — Borders, dividers
- **Line Dark**: `rgba(244,241,234,0.14)` — Light borders on dark backgrounds

## Typography

### Font Families
- **Display & Headings**: Space Grotesk
  - Font weights: 400, 500, 600, 700
  - Used for: h1, h2, h3, hero text, section titles
  - Characteristics: Modern, geometric sans-serif with technical feel

- **Body & UI**: IBM Plex Sans
  - Font weights: 400, 500, 600
  - Used for: Body text, navigation, buttons, labels
  - Characteristics: Clean, legible sans-serif with excellent readability

### Font Loading
Google Fonts CDN:
```
https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap
```

### Type Scale
- **H1 (Hero)**: `clamp(2.4rem, 5vw, 3.6rem)` — Fluid sizing for hero section
- **H2 (Section)**: `clamp(1.8rem, 3.4vw, 2.5rem)` — Section headers
- **H3 (Subsection)**: `1.25rem` — Ledger items, cards
- **Body**: `1rem` — Standard text
- **Small**: `0.95rem` — Navigation, labels
- **Kicker**: `0.95rem` — Section eyebrows

### Typography Details
- **Line Height (Heading)**: 1.08
- **Line Height (Body)**: 1.6
- **Letter Spacing (Heading)**: -0.01em
- **Font Smoothing**: Antialiased for smooth rendering

## Spacing & Layout

### Container
- **Max Width**: `1180px`
- **Padding (Desktop)**: `32px`
- **Padding (Mobile)**: `20px`

### Sections
- **Vertical Padding**: `96px` per section
- **Margin Bottom (Section Head)**: `56px`

### Components
- **Button Padding**: `11px 22px`
- **Gap (Navigation)**: `34px`
- **Gap (Brand)**: `12px`
- **Small Gap**: `14px`, `16px`

## Component Styles

### Buttons
- **Primary (`.btn-primary`)**: Orange background, white text
  - Hover: Darker orange `#d8500f`
- **Ghost (`.btn-ghost`)**: Transparent, charcoal border and text
  - Hover: Orange border and text

### Navigation
- **Style**: Sticky header with backdrop blur
- **Background**: `rgba(247,244,238,0.92)` with `backdrop-filter: blur(8px)`
- **Border**: 1px solid `--line`

### Dot Trail
- Pattern of 4 rotated squares (45°) in alternating orange/charcoal
- Used as visual accent/eyebrow element

### Ledger List
- Services display as rows with borders
- Layout: Label (280px) + Description (1fr) on desktop
- Single column on mobile

### Industry Rows
- Left border accent (3px) that changes color on hover
- Hover state includes left border color change to orange + light background tint

## Design Patterns

### Hero Section
- Navy deep background with gradient shape overlay (orange to amber)
- Overlay opacity: 0.9 with additional dark gradient overlay
- Content positioned relative with z-index: 2

### Section Headers (Kicker + Title + Description)
- Kicker: Orange, Space Grotesk, 0.95rem, 600 weight
- Title: Space Grotesk, responsive font size
- Description: Slate color, readable width (56ch max)

### Dot Trail Motif
- Inline flex with 6px gaps
- Rotated squares (7x7px)
- Sequential opacity: 100%, 85%, 60%, 40%
- Colors alternate: orange, charcoal, orange, charcoal

## Responsive Design

### Breakpoints
- **Mobile**: Default
- **Tablet/Desktop**: `min-width: 640px`, `min-width: 760px`, `min-width: 800px`, `min-width: 880px`, `min-width: 900px`

### Fluid Typography
- Uses `clamp()` for responsive font sizing
- Example: `clamp(2.4rem, 5vw, 3.6rem)` scales smoothly between viewport sizes

### Grid Layouts
- 1 column on mobile
- 2+ columns on larger screens
- Gap: 40px+ between columns

## Visual Hierarchy

1. **H1**: Largest, Navy Deep or Cream background, primary message
2. **H2**: Section titles, Space Grotesk, responsive size
3. **H3**: Subsection titles, secondary content
4. **Body**: Standard text, supporting information
5. **Small/Labels**: Navigation, metadata

## Interactive States

### Hover Effects
- Color transitions: 0.2s ease
- Border color transitions: 0.2s ease
- Transform: 0.15s ease (for buttons)
- Navigation links: Color change to orange

### Focus States
- Maintained through standard browser defaults
- Ensure sufficient contrast for accessibility

## Accessibility

- **Color Contrast**: All text meets WCAG AA standards
- **Font Rendering**: Antialiased for accessibility
- **Font Sizes**: Minimum 14px for body text
- **Responsive**: Mobile-first approach ensures usability on all devices

## Implementation Notes

- **Border Radius**: Minimal (2px) for modern, minimal aesthetic
- **Z-index**: Sticky header uses z-index: 50, hero shapes use z-index: 2
- **Overflow**: Hero section has `overflow: hidden` to contain shapes
- **Scroll Behavior**: `scroll-behavior: smooth` for smooth scrolling navigation

## Motion & Animation

- **Transition Timing**: 0.15s - 0.2s for smooth, responsive feel
- **Easing**: `ease` function for natural motion
- **Hover States**: Quick, subtle feedback without jarring changes

---

**Last Updated**: 2026-09-16
**Version**: 2.0 (Single-Page Website)
