class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        from collections import Counter

        word_freq = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            count = 0
            seen = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # Too many occurrences of this word
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Found valid concatenation
                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = right

        return result
