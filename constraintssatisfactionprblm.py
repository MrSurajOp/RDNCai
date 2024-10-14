from collections import deque, defaultdict

def find_word_ladder(start_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return None

    queue = deque([(start_word, [start_word])])
    visited = set([start_word])
    word_len = len(start_word)
    word_dict = defaultdict(list)

    for word in word_list:
        for i in range(word_len):
            word_dict[word[:i] + '*' + word[i + 1:]].append(word)

    while queue:
        current_word, ladder = queue.popleft()

        for i in range(word_len):
            intermediate_word = current_word[:i] + '*' + current_word[i + 1:]

            for word in word_dict[intermediate_word]:
                if word == end_word:
                    return ladder + [end_word]
                if word not in visited:
                    visited.add(word)
                    queue.append((word, ladder + [word]))

            word_dict[intermediate_word] = []

    return None

word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
start_word = "hit"
end_word = "cog"
result = find_word_ladder(start_word, end_word, word_list)

if result:
    print("Shortest word ladder:")
    for word in result:
        print(word)
else:
    print("No transformation sequence found.")
