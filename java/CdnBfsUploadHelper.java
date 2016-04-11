package com.bilibili.travel.helper;

import com.bilibili.travel.dashboard.helper.ApiSignHelper;
import com.bilibili.utils.StringUtils;
import net.sf.json.JSONObject;
import org.apache.http.NameValuePair;
import org.apache.http.message.BasicNameValuePair;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import sun.misc.BASE64Encoder;

import javax.crypto.Mac;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.ProtocolException;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.text.SimpleDateFormat;
import java.util.*;

/**
 * Created by bilibili_ on 2016/2/26.
 */
public class CdnBfsUploadHelper {
    protected static Logger logger = LoggerFactory.getLogger(CdnBfsUploadHelper.class);
    private static String BFS_DOMAIN = "http://bfs.bilibili.co";
    private static String BUCKET_NAME = "travel";
    private static String ACCESS_KEY = "9fb01bfd55d4f9d5";
    private static String ACCESS_SECRET = "9d78be59b521accd233b6c46f96f15";

    public static void main(String args[]) {
        JSONObject json;
        json = upload(new File("C://100_i.jpg"),null);
        json = delete("ab2c8b104fda05be68fc482b772749eae9be906a.jpg");
        System.out.println(json);
    }

    /**
     * 上传文件
     *
     * @param file
     * @param path 可以为空，或者自定义一个访问相对路径 ： abc/example.txt
     * @return
     */
    public static JSONObject upload(File file, String path) {
        String requestMethod = "PUT";
        FileInputStream fileIS = null;
        DataOutputStream out = null;
        JSONObject resultJson = new JSONObject();
        HttpURLConnection httpCon = null;
        try {
            if (file == null || !file.exists()) {
                resultJson.put("code", "-1");
                resultJson.put("message", "upload file not found");
                return resultJson;
            }

            path = reFormatPath(path);
            URL url = new URL(getRequestPrefix() + path);
            httpCon = (HttpURLConnection) url.openConnection();
            setRequestHeader(httpCon, file, path, requestMethod);
            pushFileToRequestBody(httpCon, out, fileIS, file);
            wrapResponse(resultJson, httpCon);
            return resultJson;
        } catch (Exception e) {
            logger.error("请求出错", e);
            resultJson.put("code", "1");
            resultJson.put("message", "IO EXCEPTION");
            return resultJson;
        } finally {
            try {
                if (fileIS != null)
                    fileIS.close();
                if (out != null)
                    out.close();
            } catch (IOException e) {
                logger.error("出错", e);
            }
            if (httpCon != null) {
                httpCon.disconnect();
                httpCon = null;
            }
        }
    }

    /**
     * 将文件写入请求的body之中
     *
     * @param httpCon
     * @param out
     * @param fileIS
     * @param file
     * @throws IOException
     */
    private static void pushFileToRequestBody(HttpURLConnection httpCon, DataOutputStream out, FileInputStream fileIS, File file) throws IOException {
        httpCon.setDoOutput(true);
        out = new DataOutputStream(httpCon.getOutputStream());
        byte[] buffer = new byte[1024];
        int len = 0;
        fileIS = new FileInputStream(file);
        while ((len = fileIS.read(buffer)) != -1) {
            out.write(buffer, 0, len);
        }
        out.write("\r\n".getBytes());
        out.flush();
        out.close();
    }

    /**
     * 删除服务器上的文件
     *
     * @param relativePath 文件的名字： example.txt
     * @return
     */
    public static JSONObject delete(String relativePath) {
        String requestMethod = "DELETE";
        JSONObject resultJson = new JSONObject();
        String requestURL = null;
        HttpURLConnection httpCon = null;

        if (StringUtils.isEmpty(relativePath)) {
            resultJson.put("code", "-1");
            resultJson.put("message", "relativePath cannot be empty");
            return resultJson;
        }

        try {
            relativePath = reFormatPath(relativePath);
            requestURL = getRequestPrefix() + relativePath;
            URL url = new URL(requestURL);
            httpCon = (HttpURLConnection) url.openConnection();
            setRequestHeader(httpCon, null, relativePath, requestMethod);
            if (wrapResponse(resultJson, httpCon)) return resultJson;
            return resultJson;
        } catch (Exception e) {
            logger.error("出错", e);
            resultJson.put("code", "1");
            resultJson.put("message", "IO EXCEPTION");
            return resultJson;
        } finally {
            if (httpCon != null) {
                httpCon.disconnect();
                httpCon = null;
            }
        }
    }

    /**
     * 将路径的前置 “/”,以及最后的"/" 去掉
     *
     * @param relativePath
     * @return
     */
    private static String reFormatPath(String relativePath) throws Exception {
        if (StringUtils.isEmpty(relativePath)) {
            return "";
        }
        if (relativePath.startsWith("/")) {
            relativePath = relativePath.substring(1, relativePath.length());
        }
        if (StringUtils.isEmpty(relativePath)) {
            return relativePath;
        }
        if (relativePath.endsWith("/")) {
            relativePath = relativePath.substring(0, relativePath.length() - 1);
        }

        if (relativePath != null && relativePath.contains("/")) {
            throw new Exception("第一个版本不支持带目录的上传路径");
        }
        return relativePath;
    }

    /**
     * 根据BFS文档约定生成请求头
     *
     * @param httpCon
     * @param file
     * @param path
     * @param requestMethod
     * @throws ProtocolException
     */
    private static void setRequestHeader(HttpURLConnection httpCon, File file, String path, String requestMethod) throws Exception {
        Calendar now = Calendar.getInstance();
        long expires = now.getTime().getTime() / 1000;
        String token = requestMethod + "\n" + BUCKET_NAME + "\n" + path + "\n" + expires + "\n";
        String authorization = "";
        String contentType = "";
        try {
            String result = encryptTokenWithHmacSha1(token);
            authorization = ACCESS_KEY + ":" + result + ":" + expires;
        } catch (Exception e) {
            logger.error("加密出错", e);
        }
        SimpleDateFormat greenwichDate = new SimpleDateFormat("EEE, d MMM yyyy HH:mm:ss 'GMT'", Locale.US);
        greenwichDate.setTimeZone(TimeZone.getTimeZone("GMT"));

        httpCon.setRequestProperty("Host", "bfs.bilibili.co");
        httpCon.setRequestProperty("Date", greenwichDate.format(now.getTime()));
        httpCon.setRequestProperty("Authorization", authorization);
        if (file != null) {
            contentType = Files.probeContentType(Paths.get(file.getPath()));
            httpCon.setRequestProperty("Content-Type", contentType);
            httpCon.setRequestProperty("Content-Length", Long.toString(file.length()));
        }
        httpCon.setRequestMethod(requestMethod);

        printDebugInfo(file, contentType, httpCon, now, greenwichDate, authorization, ACCESS_KEY, ACCESS_SECRET, token);
    }

    /**
     * 打印请求时的关键属性
     *
     * @param file
     * @param contentType
     * @param httpCon
     * @param now
     * @param greenwichDate
     * @param authorization
     * @param accesskey
     * @param accessSecret
     * @param data
     */
    private static void printDebugInfo(File file, String contentType, HttpURLConnection httpCon, Calendar now, SimpleDateFormat greenwichDate, String authorization, String accesskey, String accessSecret, String data) {
        System.out.println("URL：" + httpCon.getURL());
        System.out.println("Host：" + "bfs.bilibili.co");
        System.out.println("Date：" + greenwichDate.format(now.getTime()));
        System.out.println("ACCESS_KEY：" + accesskey);
        System.out.println("ACCESS_SECRET：" + accessSecret);
        System.out.println("data：" + data.replaceAll("\n", "\\\\n"));
        System.out.println("Authorization：" + authorization);
        System.out.println("Content-Type：" + contentType);
        System.out.println("Content-Length：" + (file == null ? "" : Long.toString(file.length())));
    }

    /**
     * 根据返回的header得到的信息， 包装成json返回上级请求。
     *
     * @param resultJson
     * @param httpCon
     * @return
     * @throws IOException
     */
    private static boolean wrapResponse(JSONObject resultJson, HttpURLConnection httpCon) throws IOException {
        int cah = httpCon.getResponseCode();

        if (cah == 401) {
            resultJson.put("code", "1");
            resultJson.put("message", "连接BFS服务失败，鉴权失败");
            return true;
        }

        if (cah != 200) {
            resultJson.put("code", "1");
            resultJson.put("message", "upload fail" + cah);
            return true;
        }

        Map<String, List<String>> map = httpCon.getHeaderFields();
        if (map != null) {
            resultJson.put("Code", map.get("Code"));
            resultJson.put("Location", map.get("Location"));
            resultJson.put("Etag", map.get("Etag"));
        }

        printDebugHeaderInfo(map);
        return false;
    }

    /**
     * 打印服务器返回的header信息，  上线时需要删除该方法。
     *
     * @param map
     */
    private static void printDebugHeaderInfo(Map<String, List<String>> map) {
        System.out.println("\n显示响应Header信息...");
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            System.out.println("Key : " + entry.getKey() +
                    " ,Value : " + entry.getValue());
        }
    }

    private static String encryptTokenWithHmacSha1(String data) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException {
        SecretKey secretKey = new SecretKeySpec(ACCESS_SECRET.getBytes("UTF-8"), "HmacSHA1");
        Mac mac = Mac.getInstance(secretKey.getAlgorithm());
        mac.init(secretKey);
        byte[] digest = mac.doFinal(data.getBytes("UTF-8"));
        return (new BASE64Encoder()).encode(digest);
    }

    private static String getRequestPrefix() {
        return BFS_DOMAIN + "/" + BUCKET_NAME + "/";
    }


}
