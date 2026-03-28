#!/bin/bash
# Editor Pro Max - Render Helper
# Usage: ./scripts/render.sh <composition-id> [platform]
#
# Examples:
#   ./scripts/render.sh Showcase
#   ./scripts/render.sh TikTok tiktok
#   ./scripts/render.sh Presentation youtube

COMP_ID=${1:-"Showcase"}
PLATFORM=${2:-"default"}

case $PLATFORM in
  tiktok|instagram_reel|instagram_story|youtube_short)
    WIDTH=1080
    HEIGHT=1920
    ;;
  instagram_post|twitter|facebook|square)
    WIDTH=1080
    HEIGHT=1080
    ;;
  youtube|linkedin|landscape)
    WIDTH=1920
    HEIGHT=1080
    ;;
  cinematic)
    WIDTH=1920
    HEIGHT=800
    ;;
  *)
    WIDTH=""
    HEIGHT=""
    ;;
esac

OUTPUT_DIR="out"
mkdir -p "$OUTPUT_DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_FILE="${OUTPUT_DIR}/${COMP_ID}_${PLATFORM}_${TIMESTAMP}.mp4"

echo "Rendering: ${COMP_ID}"
echo "Platform: ${PLATFORM}"
echo "Output: ${OUTPUT_FILE}"
echo ""

if [ -n "$WIDTH" ]; then
  echo "Running: npx remotion render ${COMP_ID} ${OUTPUT_FILE} --width ${WIDTH} --height ${HEIGHT}"
  npx remotion render "${COMP_ID}" "${OUTPUT_FILE}" --width "${WIDTH}" --height "${HEIGHT}"
else
  echo "Running: npx remotion render ${COMP_ID} ${OUTPUT_FILE}"
  npx remotion render "${COMP_ID}" "${OUTPUT_FILE}"
fi

echo ""
echo "Done! Output: ${OUTPUT_FILE}"
