import java.util.HashSet;
import java.util.Set;

public class BadUser {

    private final Set<Set<String>> answer = new HashSet<>();
    private final Set<String> candidate = new HashSet<>();
    private boolean[] visitedUser;
    private String[] userId;
    private String[] bannedId;

    public int solution(String[] user_id, String[] banned_id) {
        userId = user_id;
        bannedId = banned_id;
        visitedUser = new boolean[userId.length];

        dfs(0);

        return answer.size();
    }

    private void dfs(int index) {
        if (index == bannedId.length) {
            answer.add(new HashSet<>(candidate));
            return;
        }
        String bannedUser = bannedId[index];
        for (int i = 0; i < userId.length; i++) {
            String user = userId[i];
            if (user.length() != bannedUser.length() || visitedUser[i]) {
                continue;
            }
            if (equalsUser(bannedUser, user)) {
                visitedUser[i] = true;
                candidate.add(user);
                dfs(index + 1);
                candidate.remove(user);
                visitedUser[i] = false;
            }
        }
    }

    private boolean equalsUser(String bannedUser, String user) {
        for (int j = 0; j < user.length(); j++) {
            char bannedType = bannedUser.charAt(j);
            if (user.charAt(j) != bannedType && bannedType != '*') {
                return false;
            }
        }
        return true;
    }

}
