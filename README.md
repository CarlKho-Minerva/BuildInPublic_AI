# Building in Public - Automated Posting

This project aims to automate my building in public workflow, streamlining content creation and distribution across multiple platforms.  It leverages AI and several APIs to optimize content and automate uploads, freeing up my time to focus on content creation itself.  This document outlines the project's workflow, proposed features, platform considerations, media management strategy, and potential branching strategy for development.

## Workflow

1. **Input:** A video file (initially uploaded manually, with future Loom API integration as a goal). The video will be transcribed using the Whisper API.
2. **AI Content Generation:** The generated transcript will be fed into an AI model to create optimized written content for different platforms:
    * **Medium:** Algorithm-optimized for maximum reach.
    * **Substack:** Personal and reflective style.
    * **Web Blog/Portfolio:** GDE-focused, showcasing relevant skills and experience.
    * **LinkedIn:** Professional and non-cringeworthy.
    * **Twitter/X:** Short, engaging, with a link to the original video.
3. **Media Placeholders:** The AI-generated content will include designated placeholders for images, GIFs, or code snippets. These will follow a consistent format, for example: `[add screenshot or gif of "feature x" here]` or `[insert code snippet demonstrating "function y" here]`.
4. **Automated Uploads:**
    * **YouTube:** Video upload with optimized title, description, and tags.
    * **TikTok:** Video upload, potentially using a service like VideoPie for aspect ratio conversion (16:9 to 9:16) and subtitle addition.


## Features

* **AI-Powered Content Optimization:** Generate platform-specific content from video transcripts.
* **Automated Publishing:** Automatically publish content to Medium, Substack, and a personal blog.
* **Social Media Integration:** Automated posting to LinkedIn, Twitter/X, YouTube, and TikTok.
* **Media Placeholders:**  Designated locations within the text for manual media insertion after content generation.
* **Subtitle Generation & Integration:** (Optional) Generate and add subtitles to videos for accessibility.

## Platform Considerations

* **Medium:** Focus on algorithmic optimization for discoverability.
* **Substack:** Personal, reflective style, building community.
* **Web Blog/Portfolio:** Showcase technical skills and projects relevant to the Google Cloud Developer Expert program.
* **LinkedIn:** Professional networking, thought leadership, career development.
* **Twitter/X:** Short-form content, engagement, driving traffic to other platforms.
* **YouTube:** SEO optimization, building a video library, community engagement.
* **TikTok:** Short, engaging videos optimized for the platform’s algorithm.

## Media Management

Media will be managed using text placeholders within the generated content.  This simple approach removes the need for complex cloud storage solutions initially.  The user will manually add the corresponding media during the final review and publishing process.  Examples of placeholders:

* `[add screenshot or gif of "feature x" here]`
* `[insert code snippet demonstrating "function y" here]`

## Development Branching Strategy

The project can be broken down into the following branches/tasks:

**1. Core Functionality (Main Branch):**

* **Task:** Develop the core workflow: video upload, transcription, AI content generation.
* **Test Conditions:** Verify successful transcription and content generation across all platforms.

**2. Platform Optimization (Platform Branches):**

* **Task:** Refine the AI models for each platform's specific requirements (e.g., tone, style, SEO).
* **Test Conditions:**  Evaluate the quality and effectiveness of the generated content for each platform.  A/B testing can be used for platforms like Medium and Twitter/X to measure engagement.

**3. Media Management (Media Branch):**

* **Task:** Implement the media management system (placeholders, storage, linking).
* **Test Conditions:** Ensure correct placement of media in published content.

**4. Automated Uploads (Upload Branches):**

* **Task:** Integrate APIs for automated uploads to YouTube, TikTok, and other platforms. This will include optimizing video titles, descriptions, and tags based on existing best practices.  Research and incorporate appropriate video codecs and resolutions. 
* **Test Conditions:** Verify successful uploads and ensure proper metadata is included.

**5. Subtitle Generation and Integration (Subtitle Branch):**

* **Task:** Implement subtitle generation and integration into the video upload process.
* **Test Conditions:** Verify accurate subtitle generation and synchronization with the uploaded videos.
