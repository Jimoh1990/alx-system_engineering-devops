# Set the file path for the file we want to edit
$file_to_edit = '/var/www/html/wp-settings.php'

# Use sed to replace the line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin', '/usr/bin']
}
