/*
 * t1-faker edge-case demo (C)
 * Goal: exercise comments, strings, numbers, keywords, preproc, types, errors.
 */

#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>

#define CLAMP(x, lo, hi) ((x) < (lo) ? (lo) : ((x) > (hi) ? (hi) : (x)))

typedef struct {
  uint32_t id;
  const char *name;
  int32_t score;
  bool alive;
} player_t;

static uint32_t parse_u32(const char *s, bool *ok) {
  uint32_t v = 0U;
  *ok = true;

  if (!s || !*s) {
    *ok = false;
    return 0U;
  }

  for (const char *p = s; *p; ++p) {
    if (*p < '0' || *p > '9') {
      *ok = false;
      return 0U;
    }
    v = v * 10U + (uint32_t)(*p - '0');
  }

  return v;
}

int main(void) {
  player_t p = { .id = 1U, .name = "Faker", .score = 999, .alive = true };

  bool ok = false;
  uint32_t x = parse_u32("12345", &ok);

  if (!ok) {
    fprintf(stderr, "parse failed\n");
    return 2;
  }

  int32_t boosted = (int32_t)CLAMP((int32_t)x + p.score, 0, 100000);
  printf("player=%s id=%u boosted=%d alive=%s\n",
         p.name, p.id, boosted, p.alive ? "true" : "false");

  // Intentional edge cases
  const char *bad = "12a";
  (void)parse_u32(bad, &ok);
  if (ok) { /* unreachable */ }

  return 0;
}
