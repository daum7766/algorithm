import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class PillarAndBoard {

    private static final int 기둥 = 0;
    private static final int 보 = 1;
    private static final int 설치 = 1;

    private final Set<Frame> build = new HashSet<>();

    public int[][] solution(int n, int[][] build_frame) {
        for (int[] buildFrame : build_frame) {
            Frame frame = new Frame(buildFrame[0], buildFrame[1], buildFrame[2]);
            if (buildFrame[3] == 설치) {
                if (isBuildFrame(frame)) {
                    build.add(frame);
                }
            } else {
                build.remove(frame);
                if (!isRemoveBuildFrame()) {
                    build.add(frame);
                }
            }
        }
        List<Frame> frames = new ArrayList<>(build);
        Collections.sort(frames);
        int[][] answer = new int[frames.size()][3];

        for (int i = 0; i < frames.size(); i++) {
            Frame frame = frames.get(i);
            answer[i][0] = frame.getX();
            answer[i][1] = frame.getY();
            answer[i][2] = frame.getFrameType();
        }
        return answer;
    }

    private boolean isBuildFrame(Frame frame) {
        if (frame.getFrameType() == 기둥) {
            return frame.getY() == 0
                || build.contains(frame.left(보))
                || build.contains(frame.down(기둥))
                || build.contains(frame.currentOtherType());
        } else {
            return build.contains(frame.down(기둥)) || build.contains(frame.rightDown())
                || (build.contains(frame.left(보)) && build.contains(frame.right(보)));
        }
    }

    private boolean isRemoveBuildFrame() {
        List<Frame> frames = new ArrayList<>(build);
        for (Frame frame : frames) {
            if (!isBuildFrame(frame)) {
                return false;
            }
        }
        return true;
    }

    private static class Frame implements Comparable<Frame> {

        private final int x;
        private final int y;
        private final int frameType;

        public Frame(int x, int y, int frameType) {
            this.y = y;
            this.x = x;
            this.frameType = frameType;
        }

        public Frame left(int type) {
            return new Frame(x - 1, y, type);
        }

        public Frame down(int type) {
            return new Frame(x, y - 1, type);
        }

        public Frame right(int type) {
            return new Frame(x + 1, y, type);
        }

        public Frame rightDown() {
            return new Frame(x + 1, y - 1, 기둥);
        }

        public Frame currentOtherType() {
            return new Frame(x, y, Math.abs(frameType - 1));
        }

        public int getY() {
            return y;
        }

        public int getX() {
            return x;
        }

        public int getFrameType() {
            return frameType;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }
            Frame frame = (Frame) o;
            return x == frame.x && y == frame.y && frameType == frame.frameType;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, frameType);
        }

        @Override
        public int compareTo(Frame o) {
            if (x == o.x) {
                if (y == o.y) {
                    return frameType - o.frameType;
                } else {
                    return y - o.y;
                }
            }
            return x - o.x;
        }
    }
}
