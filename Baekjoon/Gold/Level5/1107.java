package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader bufferedReader =
        new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int targetChannel = Integer.parseInt(bufferedReader.readLine());

        System.out.println(findButtonChannelCount(targetChannel));
    }

    private static int findButtonChannelCount(int targetChannel) throws IOException {
        boolean[] brokenButtons = getButtonInfo();
        int answer = findPlusMinusChannelCount(100, targetChannel);

        for (int i = 0; i < 1000000; i++) {
            String channel = String.valueOf(i);

            if (buttonCheck(brokenButtons, channel)) {
                int count = findPlusMinusChannelCount(i, targetChannel) + channel.length();
                answer = Math.min(answer, count);
            }
        }

        return answer;
    }

    private static boolean buttonCheck(boolean[] brokenButtons, String channel) {
        for (int i = 0; i < channel.length(); i++) {
            int index = channel.charAt(i) - '0';

            if (brokenButtons[index]) {
                return false;
            }
        }
        return true;
    }

    private static int findPlusMinusChannelCount(int currentChannel, int targetChannel) {
        return Math.abs(currentChannel - targetChannel);
    }

    private static boolean[] getButtonInfo() throws IOException {
        boolean[] brokenButtons = new boolean[10];

        int size = Integer.parseInt(bufferedReader.readLine());
        if (size == 0) {
            return brokenButtons;
        }

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine(), " ");
        for (int i = 0; i < size; i++) {
            brokenButtons[Integer.parseInt(stringTokenizer.nextToken())] = true;
        }
        return brokenButtons;
    }
}