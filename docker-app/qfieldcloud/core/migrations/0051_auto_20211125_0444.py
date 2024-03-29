# Generated by Django 3.2.9 on 2021-11-25 03:44

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0050_auto_20211118_1150"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="packagejob",
            options={
                "verbose_name": "Job: package",
                "verbose_name_plural": "Jobs: package",
            },
        ),
        migrations.AddField(
            model_name="delta",
            name="new_geom",
            field=django.contrib.gis.db.models.fields.GeometryField(
                dim=4, null=True, srid=4326
            ),
        ),
        migrations.AddField(
            model_name="delta",
            name="old_geom",
            field=django.contrib.gis.db.models.fields.GeometryField(
                dim=4, null=True, srid=4326
            ),
        ),
        migrations.RunSQL(
            r"""
                WITH subquery AS (
                    SELECT
                        id,
                        CASE
                            WHEN jsonb_extract_path_text(content, 'localLayerCrs') ~ '^EPSG:\d{1,10}$'
                            THEN
                                REGEXP_REPLACE(jsonb_extract_path_text(content, 'localLayerCrs'), '\D*', '', 'g')::int
                            ELSE
                                NULL
                        END AS srid
                    FROM core_delta
                )
                UPDATE core_delta
                SET
                    old_geom =
                        ST_Transform(
                            ST_SetSRID(
                                ST_Force2D(
                                    ST_GeomFromText(
                                        REPLACE( jsonb_extract_path_text(core_delta.content, 'old', 'geometry'), 'nan', '0' )
                                    )
                                ),
                                subquery.srid
                            ),
                            4326
                        ),
                    new_geom =
                        ST_Transform(
                            ST_SetSRID(
                                ST_Force2D(
                                    ST_GeomFromText(
                                        REPLACE( jsonb_extract_path_text(core_delta.content, 'new', 'geometry'), 'nan', '0' )
                                    )
                                ),
                                subquery.srid
                            ),
                            4326
                        )
                FROM subquery
                WHERE core_delta.id = subquery.id
            """,
            migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            r"""
                CREATE FUNCTION core_delta_geom_trigger_func()
                RETURNS trigger
                AS
                $$
                    DECLARE
                        srid int;
                    BEGIN
                        SELECT CASE
                            WHEN jsonb_extract_path_text(NEW.content, 'localLayerCrs') ~ '^EPSG:\d{1,10}$'
                            THEN
                                REGEXP_REPLACE(jsonb_extract_path_text(NEW.content, 'localLayerCrs'), '\D*', '', 'g')::int
                            ELSE
                                NULL
                            END INTO srid;
                        NEW.old_geom := ST_Transform( ST_SetSRID( ST_Force2D( ST_GeomFromText( REPLACE( jsonb_extract_path_text(NEW.content, 'old', 'geometry'), 'nan', '0' ) ) ), srid ), 4326 );
                        NEW.new_geom := ST_Transform( ST_SetSRID( ST_Force2D( ST_GeomFromText( REPLACE( jsonb_extract_path_text(NEW.content, 'new', 'geometry'), 'nan', '0' ) ) ), srid ), 4326 );
                        RETURN NEW;
                    END;
                $$
                LANGUAGE PLPGSQL
            """,
            r"""
                DROP FUNCTION core_delta_geom_trigger_func();
            """,
        ),
        migrations.RunSQL(
            r"""
                CREATE TRIGGER core_delta_geom_update_trigger BEFORE UPDATE ON core_delta
                FOR EACH ROW
                WHEN (OLD.content IS DISTINCT FROM NEW.content)
                EXECUTE FUNCTION core_delta_geom_trigger_func()
            """,
            r"""
                DROP TRIGGER core_delta_geom_update_trigger ON core_delta;
            """,
        ),
        migrations.RunSQL(
            r"""
                CREATE TRIGGER core_delta_geom_insert_trigger BEFORE INSERT ON core_delta
                FOR EACH ROW
                EXECUTE FUNCTION core_delta_geom_trigger_func()
            """,
            r"""
                DROP TRIGGER core_delta_geom_insert_trigger ON core_delta
            """,
        ),
    ]
