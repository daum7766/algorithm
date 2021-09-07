import java.util.ArrayList;
import java.util.List;

public class NewIdCandidate {

    public String solution(String new_id) {
        return step(new_id);
    }

    public String step(String id) {
        String newId = id.toLowerCase();
        return step2(newId);
    }

    public String step2(String id) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < id.length(); i++) {
            char c = id.charAt(i);
            if (('0' <= c && '9' >= c) || ('a' <= c && 'z' >= c) || c == '-' || c == '_' || c == '.') {
                stringBuilder.append(c);
            }
        }
        return step3And4(stringBuilder.toString());
    }

    public String step3And4(String id) {
        List<Character> newId = new ArrayList<>();
        for (int i = 0; i < id.length(); i++) {
            char c = id.charAt(i);
            if (newId.isEmpty() || c != '.' || newId.get(newId.size() - 1) != '.') {
                newId.add(c);
            }
        }
        if (!newId.isEmpty() && newId.get(0) == '.') {
            newId.remove(0);
        }
        if (!newId.isEmpty() && newId.get(newId.size() - 1) == '.') {
            newId.remove(newId.size() - 1);
        }

        StringBuilder stringBuilder = new StringBuilder();
        for (char c : newId) {
            stringBuilder.append(c);
        }
        return step5(stringBuilder.toString());
    }

    public String step5(String id) {
        if ("".equals(id)) {
            id = "a";
        }
        return step6(id);
    }

    public String step6(String id) {
        int limitSize = 15;
        if (id.length() > limitSize) {
            id = id.substring(0, limitSize);
        }
        while (id.charAt(id.length() - 1) == '.') {
            id = id.substring(0, id.length() - 1);
        }
        return step7(id);
    }

    public String step7(String id) {
        StringBuilder idBuilder = new StringBuilder(id);
        while (idBuilder.length() < 3) {
            idBuilder.append(idBuilder.charAt(idBuilder.length() - 1));
        }
        return idBuilder.toString();
    }
}
