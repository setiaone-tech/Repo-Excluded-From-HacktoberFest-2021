class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      prefix = ''
      for arr in zip(*strs):
        if len(set(arr)) > 1:
          break
        prefix += arr[0]
      return prefix
